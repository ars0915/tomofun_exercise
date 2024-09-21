import aws_cdk as core
import aws_cdk.assertions as assertions

from tomofun_exercise.tomofun_exercise_stack import TomofunExerciseStack

# example tests. To run these tests, uncomment this file along with the example
# resource in tomofun_exercise/tomofun_exercise_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TomofunExerciseStack(app, "tomofun-exercise")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
