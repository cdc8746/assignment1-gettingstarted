### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    match question:
        case 'In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?':
            return 'pcap'
        case "Are encoding and encryption the same? - Yes/No":
            return 'No'
        case "Is it possible to decrypt a message without a key? - Yes/No":
            return 'No'
        case "Is it possible to decode a message without a key? - Yes/No":
            return 'Yes'
        case "Is a hashed message supposed to be un-hashed? - Yes/No":
            return 'No'
        case "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
            return '368f3ef1a4c7c03ab3c9be1a8b4837e67cd1775a385cb1306d49b3e50323b2a5'
        case "Is MD5 a secured hashing algorithm? - Yes/No":
            return 'No'
        case "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
            return '4'
        case "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
            return '2'
    
if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question1 = welcome_assignment_answers("In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?")
    debug_question1 = welcome_assignment_answers("Are encoding and encryption the same? - Yes/No")
    debug_question1 = welcome_assignment_answers("Is it possible to decrypt a message without a key? - Yes/No")
    debug_question1 = welcome_assignment_answers("Is it possible to decode a message without a key? - Yes/No")
    debug_question1 = welcome_assignment_answers("Is a hashed message supposed to be un-hashed? - Yes/No")
    debug_question1 = welcome_assignment_answers("What is the SHA256 hashing value of your NYU email and use the answer in your code - ")
    debug_question1 = welcome_assignment_answers("Is MD5 a secured hashing algorithm? - Yes/No")
    debug_question1 = welcome_assignment_answers("What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number")
    debug_question1 = welcome_assignment_answers("What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number")
    
#Questions:
# "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
# "Are encoding and encryption the same? - Yes/No":
# "Is it possible to decrypt a message without a key? - Yes/No":
# "Is it possible to decode a message without a key? - Yes/No":
# "Is a hashed message supposed to be un-hashed? - Yes/No":
# "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
# "Is MD5 a secured hashing algorithm? - Yes/No":
# "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
# "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":

