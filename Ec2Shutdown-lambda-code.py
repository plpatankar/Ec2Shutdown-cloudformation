import boto3
import logging

# setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
# Use the filter() method of the instances collection to retrieve
# all running EC2 instances.
    filters = [{
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    filters_exclude = [{
            'Name': 'tag:AutoOff',
            'Values': ['False']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
# filter the instances
    instances = ec2.instances.filter(Filters=filters)
    instances_exclude = ec2.instances.filter(Filters=filters_exclude)

# locate all running instances
    RunningInstances = [instance.id for instance in instances]
    RunningInstances_exclude = [instance.id for instance in instances_exclude]
    running_count = 0
    
# print the instances for logging purposes
# print RunningInstances 
    
# make sure there are actually instances to shut down. 
    for instance in instances:
        if instance.id not in RunningInstances_exclude:
# perform the shutdown
            shuttingDown = instance.stop()
            print shuttingDown
            running_count = running_count + 1
        else:
            print "Instance %s is excluded" % instance.id

    if running_count == 0:
        print "No instance found to stop"

