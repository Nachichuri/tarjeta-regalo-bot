from datetime import datetime as dt

def write_log(event, userinfo):
    event = [event,
             userinfo.username,
             userinfo.is_bot,
             userinfo.first_name,
             userinfo.last_name,
             userinfo.id,
             userinfo.language_code]

    with open('log.txt', 'a') as log_file:
        log_file.write('\t'.join([str(x) for x in event]) + '\t' + dt.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
