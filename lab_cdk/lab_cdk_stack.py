from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw,  
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    RemovalPolicy
)
from constructs import Construct

class LabCdkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Bucket S3 pour site statique
        bucket = s3.Bucket(
            self, "WebsiteBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            website_index_document="index.html"
        )

        # Fonction Lambda
        hello_lambda = lambda_.Function(
            self, "HelloHandler",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="hello.handler",
            code=lambda_.Code.from_asset("lambda")
        )

        # API Gateway
        api = apigw.LambdaRestApi(
            self, "HelloAPI",
            handler=hello_lambda,
            proxy=False
        )

        api.root.add_method("GET")

        # Déploiement du site statique 
        s3deploy.BucketDeployment(
            self, 
            "DeploySite",
            sources=[s3deploy.Source.asset("static_website")],
            destination_bucket=bucket
        )