import json
from db import get_connection

def lambda_handler(event, context):
    """
    Get voting results for a poll.

    Test event in console:
    {
      "pollId": 1
    }
    """

    poll_id = event.get("pollId")

    if not poll_id:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "pollId is required"})
        }

    try:
        poll_id = int(poll_id)
    except ValueError:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "pollId must be an integer"})
        }

    conn = get_connection()

    try:
        with conn.cursor() as cur:
            # Get poll info (title, allow_comments)
            cur.execute(
                "SELECT poll_id, title, allow_comments FROM polls WHERE poll_id=%s",
                (poll_id,)
            )
            poll = cur.fetchone()

            if not poll:
                return {
                    "statusCode": 404,
                    "headers": {"Access-Control-Allow-Origin": "*"},
                    "body": json.dumps({"error": "Poll not found"})
                }

            # Get options and vote counts
            # LEFT JOIN so options with 0 votes are still returned
            cur.execute(
                """
                SELECT o.option_id,
                       o.label,
                       COUNT(v.vote_id) AS vote_count
                FROM poll_options o
                LEFT JOIN votes v
                  ON o.option_id = v.option_id
                 AND o.poll_id = v.poll_id
                WHERE o.poll_id = %s
                GROUP BY o.option_id, o.label
                ORDER BY o.option_id
                """,
                (poll_id,)
            )
            rows = cur.fetchall()

        total_votes = sum(r["vote_count"] for r in rows)

        results = []
        for r in rows:
            count = r["vote_count"]
            percentage = (count / total_votes * 100) if total_votes > 0 else 0.0

            results.append({
                "optionId": r["option_id"],
                "label": r["label"],
                "votes": int(count),
                "percentage": round(percentage, 2)
            })

        response_body = {
            "pollId": poll["poll_id"],
            "title": poll["title"],
            "allowComments": bool(poll["allow_comments"]),
            "totalVotes": int(total_votes),
            "results": results
        }

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps(response_body)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
    finally:
        conn.close()
