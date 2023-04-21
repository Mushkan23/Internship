def convert_result_to_message(result):
    if len(result) == 0:
        return "Sorry, we currently don't have any solution or answer pertaining to your food."
    message = ""
    for data in result:
        message += f"query: {data['tag']}\n"
        message += "query\n"
        count = 1
        for step in data['response']:
            message += f"{count}. {step}\n"
            count += 1
        message += '\n\n'
    return message