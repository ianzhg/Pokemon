import json
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

##Fedex
def Fedex_api():
    url = "https://apis-sandbox.fedex.com/oauth/token"

    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    fex_account_num = os.environ.get("FEDEX_ACCOUNT")

    grant_type= f"""grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"""

    payload = grant_type # 'input' refers to JSON Payload
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    res = json.loads(response.text)
    access_token = res['access_token']
    #from this step we can get the access_token for fedex api
    input1 = {
    "accountNumber": {
        "value": fex_account_num
    },
    "requestedShipment": {
        "shipper": {
        "address": {
            "postalCode": 75063,
            "countryCode": "US"
        }
        },
        "recipient": {
        "address": {
            "postalCode": "m1m1m1",
            "countryCode": "CA"
        }
        },
        "pickupType": "DROPOFF_AT_FEDEX_LOCATION",
        "serviceType": "FEDEX_GROUND",
        "rateRequestType": [
        "LIST",
        "ACCOUNT"
        ],
        "customsClearanceDetail": {
        "dutiesPayment": {
            "paymentType": "SENDER",
            "payor": {
            "responsibleParty": None
            }
        },
        "commodities": [
            {
            "description": "Camera",
            "quantity": 1,
            "quantityUnits": "PCS",
            "weight": {
                "units": "KG",
                "value": 20
            },
            "customsValue": {
                "amount": 100,
                "currency": "USD"
            }
            }
        ]
        },
        "requestedPackageLineItems": [
        {
            "weight": {
            "units": "KG",
            "value": 20
            }
        }
        ]
    }
    }

    url = "https://apis-sandbox.fedex.com/rate/v1/rates/quotes"

    payload = input1 # 'input' refers to JSON Payload
    bearer = "Bearer "+ access_token
    headers = {
        'Content-Type': "application/json",
        'X-locale': "en_US",
        'Authorization': bearer
        }

    response = requests.post(url, data=payload, headers=headers)
return response.text


##Fedex
def DHL_api():
    dhl_id = os.environ.get("DHL_ID")
    dhl_password = os.environ.get("DHL_PASSWORD")
    dhl_account = os.environ.get("DHL_ACCOUNT")

    dhl_shipping.dhl_site_id = dhl_id
    dhl_shipping.dhl_site_password = dhl_password
    dhl_shipping.dhl_account_no = dhl_account  # set it to get correct rate

    # Spacify Maximum Execution Time (in second) - For how many second the API should try to get response from DHL (Multiprocess)
    dhl_shipping.max_response_time = 30

    # the From and to Address - only mendatory fields are provided here
    quote_address = {
        'from_country': 'AU',
        'from_city': 'Melbourne',
        'from_zipcode': '3000',

        'to_country': 'MY',
        'to_city': 'Kuala Lumpur',
        'to_zipcode': '50200'
    }

    # the unit of measurements - only mendatory fields are provided here
    quote_unit = {
        'dimension_unit': 'CM',
        'weight_unit': 'KG'
    }

    # Pieces as List of Dictionary - it can be one ore more pieces - here with two pieces example
    piece_one = {
        'piece_id': '1',
        'piece_height': '15',
        'piece_depth': '15',
        'piece_width': '15',
        'piece_weight': '1'
    }
    piece_two = {
        'piece_id': '2',
        'piece_height': '2',
        'piece_depth': '2',
        'piece_width': '2',
        'piece_weight': '2'
    }
    # Create the list with multiple (here 2) pieces
    quote_pieces = []
    quote_pieces.append(piece_one)
    quote_pieces.append(piece_two)

    # Some oter data
    quote_optional_data = {

        'is_dutiable': 'Y',  # Y|N
        'declared_currency': 'MYR',  # currency code of To Country
        'declared_value': '150.00',

        'insured_value': '100.00',   # Optional
        'insured_currency': 'MYR',   # Optional
    }

    # Finally preapre the data to send to the API
    quote_data_to_send = {
        'addresses': quote_address,
        'units': quote_unit,
        'pieces': quote_pieces,
        'optional_data': quote_optional_data,
    }

    # with the prepare data call the function and get the response
    dict_response = dhl_shipping.quote.get_quote(quote_data_to_send)
    return dict_response.text

def USPS_api():
    usps_username = os.environ.get("USPS_USERNAME")
    usps_password = os.environ.get("USPS_PASSWORD")


    now = datetime.now(pytz.utc)

    # Format the time in the desired format
    formatted_time = now_local.strftime('%Y-%m-%dT%H:%M:%S')+ "-06:00"

    #each card weight about 10lb and convert to lb
    cards_weight = 5 * 10 * 0.00220462
    # Define the API URL
    url = "https://secure.shippingapis.com/ShippingAPI.dll?"

    xml_request_body = f"""<IntlRateV2Request USERID="{usps_username}" PASSWORD="{usps_password}">

        <Revision>2</Revision>

        <Package ID="1ST">

            <Pounds>{cards_weight}</Pounds>

            <Ounces>0</Ounces>

            <Machinable>True</Machinable>

            <MailType>Package</MailType>

            <GXG>

                <POBoxFlag>Y</POBoxFlag>

                <GiftFlag>N</GiftFlag>

            </GXG>

            <ValueOfContents>100</ValueOfContents>

            <Country>Japan</Country>

            <Width>4</Width>

            <Length>5</Length>

            <Height>3</Height>

            <OriginZip>90001</OriginZip>
            <AcceptanceDateTime>{formatted_time}</AcceptanceDateTime>

            <DestinationPostalCode>100-0000</DestinationPostalCode>

        </Package>

    </IntlRateV2Request>"""
    # Define the request parameters
    params = {
        "API": "IntlRateV2",
        "XML": xml_request_body,
    }

    # Send the request to the USPS API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        from xml.etree import ElementTree

        # Parse the XML response
        root = ElementTree.fromstring(response.content)

        # Extract and print shipping quotes
        for service in root.findall(".//Service"):
            service_name = service.find("SvcDescription").text
            rate = service.find("Postage").text
            # Find the expected delivery date
            delivery_date = service.find("SvcCommitments").text

            print(f"{service_name.strip()}: ${rate}, Expected Delivery Date: {delivery_date}")
    else:
        print(f"Error: {response.status_code}")


def UPS_api():
    ups_username = os.environ.get("UPS_USERNAME")
    ups_password = os.environ.get("UPS_PASSWORD")
    ups_account_no = os.environ.get("UPS_ACCOUNT")

    url = "https://wwwcie.ups.com/security/v1/oauth/token"

    payload = {
    "grant_type": "client_credentials"
    }

    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "x-merchant-id": "string"
    }

    response = requests.post(url, data=payload, headers=headers, auth=(username,password))

    data = response.json()
    access_token = data['access_token']

    bear = "Bearer " + access_token

    version = "v1"
    requestoption = "Rate"
    url = "https://wwwcie.ups.com/api/rating/" + version + "/" + requestoption

    query = {
    "additionalinfo": "string"
    }

    payload = {
    "RateRequest": {
        "Request": {
        "TransactionReference": {
            "CustomerContext": "CustomerContext",
            "TransactionIdentifier": "TransactionIdentifier"
        }
        },
        "Shipment": {
        "Shipper": {
            "Name": "ShipperName",
            "ShipperNumber": ups_account_no,
            "Address": {
            "AddressLine": [
                "ShipperAddressLine",
                "ShipperAddressLine",
                "ShipperAddressLine"
            ],
            "City": "TIMONIUM",
            "StateProvinceCode": "MD",
            "PostalCode": "21093",
            "CountryCode": "US"
            }
        },
        "ShipTo": {
            "Name": "ShipToName",
            "Address": {
            "AddressLine": [
                "ShipToAddressLine",
                "ShipToAddressLine",
                "ShipToAddressLine"
            ],
            "City": "Alpharetta",
            "StateProvinceCode": "GA",
            "PostalCode": "30005",
            "CountryCode": "US"
            }
        },
        "ShipFrom": {
            "Name": "ShipFromName",
            "Address": {
            "AddressLine": [
                "ShipFromAddressLine",
                "ShipFromAddressLine",
                "ShipFromAddressLine"
            ],
            "City": "TIMONIUM",
            "StateProvinceCode": "MD",
            "PostalCode": "21093",
            "CountryCode": "US"
            }
        },
        "PaymentDetails": {
            "ShipmentCharge": {
            "Type": "01",
            "BillShipper": {
                "AccountNumber": ups_account_no
            }
            }
        },
        "Service": {
            "Code": "03",
            "Description": "Ground"
        },
        "NumOfPieces": "1",
        "Package": {
            "SimpleRate": {
            "Description": "SimpleRateDescription",
            "Code": "XS"
            },
            "PackagingType": {
            "Code": "02",
            "Description": "Packaging"
            },
            "Dimensions": {
            "UnitOfMeasurement": {
                "Code": "IN",
                "Description": "Inches"
            },
            "Length": "5",
            "Width": "5",
            "Height": "5"
            },
            "PackageWeight": {
            "UnitOfMeasurement": {
                "Code": "LBS",
                "Description": "Pounds"
            },
            "Weight": "1"
            }
        }
        }
    }
    }

    headers = {
    "Content-Type": "application/json",
    "transId": "string",
    "transactionSrc": "testing",
    "Authorization": bear
    }

    response = requests.post(url, json=payload, headers=headers, params=query)

    data = response.json()
    print(data)