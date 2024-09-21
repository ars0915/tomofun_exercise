from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    Duration,
)
from constructs import Construct

class TomofunExerciseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create SQS queue
        queue = sqs.Queue(
            self, "TomofunQueue",
            visibility_timeout=Duration.seconds(300)
        )

        # Create Lambda function for POST request
        post_lambda = _lambda.Function(
            self, "PostLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="post_lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "QUEUE_URL": queue.queue_url
            }
        )

        # Create Lambda function for GET request
        get_lambda = _lambda.Function(
            self, "GetLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="get_lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "QUEUE_URL": queue.queue_url
            }
        )

        # Grant permissions to Lambda functions
        queue.grant_send_messages(post_lambda)
        queue.grant_consume_messages(get_lambda)