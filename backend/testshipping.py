from shipping import fedex
from shipping import function_runner

# Call the japan_post function with specified parameters
result = function_runner(fedex, 1, jp_zipcode="120-0011", us_zipcode="90001")
# Use or print the result as needed
print(result)