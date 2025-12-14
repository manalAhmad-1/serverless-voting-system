import json
from db import get_connection

def lambda_handler(event, context):
    """
    Submit a vote for a poll option.
    Expected event format (from API Gateway):
    {
      "body": "{\"pollId\": 1, \"optionId\": 2}"
    }
    """

    # Parse the body (string JSON from API Gateway)
    body = json.loads(event.get("body", "{}"))

    poll_id = body.get("pollId")
    option_id = body.get("optionId")

    # Basic validation
    if not poll_id or not option_id:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "pollId and optionId are required"})
        }

    # Ensure they are integers
    try:
        poll_id = int(poll_id)
        option_id = int(option_id)
    except ValueError:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "pollId and optionId must be integers"})
        }

    conn = get_connection()

    try:
        with conn.cursor() as cur:
            # (Optional) verify that the option belongs to the poll
            cur.execute(
                "SELECT option_id FROM poll_options WHERE option_id=%s AND poll_id=%s",
                (option_id, poll_id)
            )
            option = cur.fetchone()

            if not option:
                return {
                    "statusCode": 404,
                    "headers": {"Access-Control-Allow-Origin": "*"},
                    "body": json.dumps({"error": "Option does not exist for this poll"})
                }

            # Insert the vote
            cur.execute(
                "INSERT INTO votes (poll_id, option_id) VALUES (%s, %s)",
                (poll_id, option_id)
            )

        conn.commit()

        return {
            "statusCode": 201,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "message": "Vote submitted",
                "pollId": poll_id,
                "optionId": option_id,
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
    finally:
        conn.close()

