## Retrieve and Generate

```json
{
  "ResponseMetadata": {
    "RequestId": "f5b05b43-43bb-4bc6-9c6e-a5458f1195fb",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "date": "Tue, 02 Jan 2024 11:01:47 GMT",
      "content-type": "application/json",
      "content-length": "586",
      "connection": "keep-alive",
      "x-amzn-requestid": "f5b05b43-43bb-4bc6-9c6e-a5458f1195fb"
    },
    "RetryAttempts": 0
  },
  "sessionId": "4fd04811-2ba3-4c18-a564-fc3d407bf150",
  "output": {
    "text": "To make a chatbot, you can use Amazon Bedrock knowledge base (version 2)."
  },
  "citations": [
    {
      "generatedResponsePart": {
        "textResponsePart": {
          "text": "To make a chatbot, you can use Amazon Bedrock knowledge base (version 2).",
          "span": {
            "start": 0,
            "end": 72
          }
        }
      },
      "retrievedReferences": [
        {
          "content": {
            "text": "\u5982\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot?  \u901a\u8fc7Amazon Bedrock knowledge base (version 2)"
          },
          "location": {
            "type": "S3",
            "s3Location": {
              "uri": "s3://aigc.red.plaza/kb/demo/chatbot/\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot1.docx"
            }
          }
        }
      ]
    }
  ]
}

```

## Only Retrieve 

```json
{
  "ResponseMetadata": {
    "RequestId": "b751e878-af53-46a5-96e0-5fafd4bd1319",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "date": "Tue, 02 Jan 2024 11:01:48 GMT",
      "content-type": "application/json",
      "content-length": "2376",
      "connection": "keep-alive",
      "x-amzn-requestid": "b751e878-af53-46a5-96e0-5fafd4bd1319"
    },
    "RetryAttempts": 0
  },
  "retrievalResults": [
    {
      "content": {
        "text": "\u5982\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot?  \u901a\u8fc7Amazon Bedrock knowledge base (version 2)"
      },
      "location": {
        "type": "S3",
        "s3Location": {
          "uri": "s3://aigc.red.plaza/kb/demo/\u5982\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot.docx"
        }
      },
      "score": 0.7278093
    },
    {
      "content": {
        "text": "\u5982\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot?  \u901a\u8fc7Amazon Bedrock knowledge base (version 2)"
      },
      "location": {
        "type": "S3",
        "s3Location": {
          "uri": "s3://aigc.red.plaza/kb/demo/chatbot/\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot1.docx"
        }
      },
      "score": 0.7278093
    },
    {
      "content": {
        "text": "\u5982\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot?  \u901a\u8fc7Amazon Bedrock knowledge base (version 2)"
      },
      "location": {
        "type": "S3",
        "s3Location": {
          "uri": "s3://aigc.red.plaza/kb/demo/chatbot/\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot3.docx"
        }
      },
      "score": 0.7278093
    },
    {
      "content": {
        "text": "\u5982\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot?  \u901a\u8fc7Amazon Bedrock knowledge base (version 2)"
      },
      "location": {
        "type": "S3",
        "s3Location": {
          "uri": "s3://aigc.red.plaza/kb/demo/\u4f55\u5feb\u901f\u5b9e\u73b0\u4e00\u4e2a\u53ef\u7528\u7684ChatBot1.docx"
        }
      },
      "score": 0.7278093
    },
    {
      "content": {
        "text": "In order to complete this quick start guide, you must have an Amazon Web Services (AWS) account.  When you sign up for AWS, your AWS account is automatically signed up for all services in AWS,  including Amazon S3. If you don't have an AWS account, use the following procedure to create one.   To sign up for AWS   1. Open https://portal.aws.amazon.com/billing/signup.   2. Follow the online instructions.   Part of the sign-up procedure involves receiving a phone call and entering a verification code  on the phone keypad.   When you sign up for an AWS account, an AWS account root user is created. The root user  has access to all AWS services and resources in the account. As a security best practice, assign  administrative access to an administrative user, and use only the root user to perform tasks  that require root user access.   This quick start guide includes the following topics:   \u2022 Step 1: Create an Amazon S3 Bucket   \u2022 Step 2: Upload a File to Your Amazon S3 Bucket   \u2022 Step 3: Retrieve a File from Your Amazon S3 Bucket   \u2022 Step 4: Delete a File From Your Amazon S3 Bucket   For more information about Amazon S3, see the Amazon Simple Storage Service Documentation."
      },
      "location": {
        "type": "S3",
        "s3Location": {
          "uri": "s3://aigc.red.plaza/kb/demo/qs-s3backup.pdf"
        }
      },
      "score": 0.57343453
    }
  ]
}

```