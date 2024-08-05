import zmq
import json

def test_affordability(monthly_income, car_payment):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    request = {
        'monthly_income': monthly_income,
        'car_payment': car_payment
    }

    print(f"Sending request: {request}")
    socket.send_json(request)

    response = socket.recv_json()
    print(f"Received response: {response}")

    socket.close()
    context.term()

    return response

# Test case 1: Affordable car
print("Test Case 1: Affordable car")
test_affordability_calculator(5000, 400)

print("\n" + "=" * 40 + "\n")

# Test case 2: Unaffordable car
print("Test Case 2: Unaffordable car")
test_affordability_calculator(3000, 500)

print("\n" + "=" * 40 + "\n")

# Test case 3: Edge case (exactly 10% of income)
print("Test Case 3: Edge case (exactly 10% of income)")
test_affordability_calculator(4000, 400)
