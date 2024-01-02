import json
import boto3

bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name="us-west-2")


# from bedrock_agent_runtime import Bedrock

def retrieveAndGenerate(input, kbId):
    """
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/retrieve_and_generate.html
    :param input:
    :param kbId:
    :return:
    """
    return bedrock_agent_runtime.retrieve_and_generate(
        input={
            'text': input
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kbId,
                'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-instant-v1'
            }
        }
    )
    return retrieveAndGenerateConfiguration


def retrieve(input, kbId):
    """
    查看  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/retrieve.html

    :param input:
    :param kbId:
    :return:
    """
    # import boto3
    return bedrock_agent_runtime.retrieve(
        knowledgeBaseId=kbId,
        retrievalQuery={
            'text': input
        }
    )
    return retrieveAndGenerateConfiguration


if __name__ == "__main__":
    response = retrieveAndGenerate('how to make a chatbot?', 'HCDTPP7B79')
    print(json.dumps(response, indent=2))

    response = retrieve('how to make a chatbot?', 'HCDTPP7B79')
    print(json.dumps(response, indent=2))
