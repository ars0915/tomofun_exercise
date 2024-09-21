# CDK SQS API Project

This project is built using AWS CDK in Python and creates an API Gateway, Lambda functions, and an SQS queue. The API allows users to send messages to and retrieve messages from an SQS queue.


## Prerequisites

1. **Install AWS CDK**: Make sure AWS CDK is installed. If not, install it using:

   ```bash
   npm install -g aws-cdk
   ```

2. **Python environment**: You need Python and virtualenv installed.

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**: Install the necessary Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS credentials**: Ensure your AWS CLI is configured properly. You can do this by running:

   ```bash
   aws configure
   ```

## Deployment

To deploy the stack, follow these steps:

1. **Synthesize the CloudFormation template**:

   ```bash
   cdk synth
   ```

2. **Deploy the stack to your AWS account**:

   ```bash
   cdk deploy
   ```

This will create:

- An API Gateway
- Two Lambda functions (for sending and retrieving messages)
- An SQS queue

Once deployed, you'll receive the API Gateway endpoint URL in the output. Use this URL to interact with the APIs.

## API Documentation

### POST `/send`

Send a message to SQS.

- **Method**: `POST`
- **URL**: `/send`
- **Request Body**:

  ```json
  {
      "message": "Your message here"
  }
  ```

- **Response**:

  - `200 OK`: Message successfully sent to SQS.
  - **Response Body**:

    ```json
    "Message sent to SQS!"
    ```

- **Example**:

  ```bash
  curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/prod/send \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from API Gateway"}'
  ```

### GET `/receive`

Retrieve a message from SQS.

- **Method**: `GET`
- **URL**: `/receive`
- **Response**:

  - `200 OK`: Successfully retrieved the message from SQS.
  - **Response Body**:

    ```json
    "Your message from SQS"
    ```

  - `404 Not Found`: No messages in SQS.
  - **Response Body**:

    ```json
    "No messages in SQS"
    ```

- **Example**:

  ```bash
  curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/prod/receive
  ```

## Cleanup

To delete the stack and clean up all resources:

```bash
cdk destroy
```