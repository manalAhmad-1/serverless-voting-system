import json
from db import get_connection

def lambda_handler(event, context):
    """
    Get details of a poll and its options.

    When testing from the console, send:
    {
      "pollId": 1
    }
    """

    poll_id = event.get("pollId")

    # Basic validation
    if not poll_id:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "pollId is required"})
        }

    # Make sure poll_id is int
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
            # Get poll
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

            # Get options
            cur.execute(
                "SELECT option_id, label FROM poll_options WHERE poll_id=%s",
                (poll_id,)
            )
            options = cur.fetchall()

        response = {
            "pollId": poll["poll_id"],
            "title": poll["title"],
            "allowComments": bool(poll["allow_comments"]),
            "options": options
        }

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps(response)
        }

    except Exception as e:
        # For debugging if needed
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
    finally:
        conn.close()
