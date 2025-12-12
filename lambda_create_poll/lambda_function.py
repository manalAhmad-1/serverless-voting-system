import json
from db import get_connection

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    title = body.get("title")
    options = body.get("options", [])
    allow_comments = body.get("allowComments", True)

    if not title or len(options) < 2:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Need title and at least 2 options"})
        }

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO polls (title, allow_comments) VALUES (%s, %s)",
                (title, allow_comments)
            )
            poll_id = cur.lastrowid

            for label in options:
                cur.execute(
                    "INSERT INTO poll_options (poll_id, label) VALUES (%s, %s)",
                    (poll_id, label)
                )

        conn.commit()

        return {
            "statusCode": 201,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "pollId": poll_id,
                "title": title,
                "options": options,
                "allowComments": allow_comments
            })
        }
    finally:
        conn.close()
