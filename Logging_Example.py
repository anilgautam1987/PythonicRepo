'''''''''''''''''''''''''''''''''''''''''''''

For Mr. PiDiddy:

Small Briefing of Using Pythonic Logging

Please Uncomment the Functions as you Explore
Different Logging Samples I Wrote To See Them
                    RUN!

Hopefully, this helps for the fundamentals

'''''''''''''''''''''''''''''''''''''''''''''

import logging

###There are Five Levels of Severity
# DEBUG     - Diagnostic Details
# INFO      - Progress Info
# WARNING   - Warning
# ERROR     - Error
# CRITICAL  - OMGOSH HALP!

###Logging Output To Console
#This is if you want stuff not in a log file

def Basic_Console_Logging():
    '''''
        Basically Output to Console with respective Severity/Message
        NOTE: By Default Output Level Threshold is WARNING, so only WARNING To ERROR Will Display
        Below you'll learn how to configure/change that!
    '''''
    logging.debug('Here is an interesting fact')
    logging.info('A male octopus had 7 tentacles, heres why...')
    logging.warning('I should not continue with that fact')
    logging.error('Someone reported this to HR!')
    logging.critical('HR Is Coming this WAY!!!!')

def Basic_ToFile_Logging():
    '''''
        Basically Logging To A File

        Basic Attr:
            filename - dir to a logfile
            filemode - how to handle log info, default 'a' (append)
            level    - threshold to log
                        (i.e. Debug will log Debug To Critical
                              Warning will log Warning To Critical
                              Critical will log only Critical)
    '''''
    logging.basicConfig(filename='nsfw.log', filemode='w', level=logging.DEBUG)

    logging.debug('Here is an interesting fact')
    logging.info('A male octopus had 7 tentacles, heres why...')
    logging.warning('I should not continue with that fact')
    logging.error('Someone reported this to HR!')
    logging.critical('HR Is Coming this WAY!!!!')

def Intermediate_With_Variables_Logging():
    '''''
            Handling Variables In Your Outputs Applies for Console/File

            Basic Attr:
                filename - dir to a logfile
                filemode - how to handle log info, default 'a' (append)
                level    - threshold to log
                            (i.e. Debug will log Debug To Critical
                                  Warning will log Warning To Critical
                                  Critical will log only Critical)
        '''''
    logging.basicConfig(filename='nsfw.log', filemode='w', level=logging.DEBUG)

    #Variables
    ANIMAL = 'Monkey'
    ANATOMOY = 'long tail'

    #Examples
    logging.debug('Here is an %s', 'interesting fact')
    logging.info('A %s had %s, heres why...', ANIMAL, ANATOMOY)

    #Same Same Same
    logging.warning('I should not continue with that fact')
    logging.error('Someone reported this to HR!')
    logging.critical('HR Is Coming this WAY!!!!')

def Intermediate_Logging_With_Time_Stamp():
    '''''
        Same as basic logging, but now you know you have control on the format
        of your output as well

        Basic Attr:
            filename - dir to a logfile
            filemode - how to handle log info, default 'a' (append)
            level    - threshold to log
                        (i.e. Debug will log Debug To Critical
                              Warning will log Warning To Critical
                              Critical will log only Critical)
            format   - format your output
            datefmt  - format the timestamp
    '''''
    logging.basicConfig(filename='nsfw.log',
                        filemode='w',
                        level=logging.DEBUG,
                        format='%(levelname)s - %(asctime)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.debug('Here is an interesting fact')
    logging.info('A male octopus had 7 tentacles, heres why...')
    logging.warning('I should not continue with that fact')
    logging.error('Someone reported this to HR!')
    logging.critical('HR Is Coming this WAY!!!!')

def Intermdeidate_Logger_Instance_Logging():
    '''''
    Incase you want a different logger with an identifier
    The Identifier helps for having different loggers
    In above exanples you might note "Root", that is the default ID

    The advance stuff for this is you'll play with you formatting
    such as the above thing examples.
    '''''

    logger = logging.getLogger('Patricks_Logger')
    logger.setLevel(logging.DEBUG)

    logger.debug('Here is an interesting fact')
    logger.info('A male octopus had 7 tentacles, heres why...')
    logger.warning('I should not continue with that fact')
    logger.error('Someone reported this to HR!')
    logger.critical('HR Is Coming this WAY!!!!')

if __name__ == '__main__':

    #Basic_Console_Logging()
    #Basic_ToFile_Logging()
    #Intermediate_With_Variables_Logging()
    #Intermediate_Logging_With_Time_Stamp()
    #Intermdeidate_Logger_Instance_Logging()
