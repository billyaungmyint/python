from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Hello World"):
    ELB("Load Balancer") >> EC2("Web Instance") >> RDS("Database")

