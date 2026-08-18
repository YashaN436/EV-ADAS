from adas.adas_engine import ADASEngine


engine = ADASEngine()


# Test 1: Safe condition
data = {
    "speed": 50,
    "battery": 80,
    "temperature": 40,
    "distance": 50
}

result = engine.check(data)

print("TEST 1")
print(result)

assert result["status"] == "SYSTEM SAFE"


# Test 2: High speed
data = {
    "speed": 85,
    "battery": 80,
    "temperature": 40,
    "distance": 50
}

result = engine.check(data)

print("\nTEST 2")
print(result)

assert "HIGH SPEED" in result["warnings"]


# Test 3: Collision warning
data = {
    "speed": 50,
    "battery": 80,
    "temperature": 40,
    "distance": 5
}

result = engine.check(data)

print("\nTEST 3")
print(result)

assert "COLLISION WARNING" in result["warnings"]


# Test 4: Multiple warnings
data = {
    "speed": 85,
    "battery": 15,
    "temperature": 60,
    "distance": 5
}

result = engine.check(data)

print("\nTEST 4")
print(result)

assert len(result["warnings"]) == 4


print("\n✅ ALL ADAS TESTS PASSED")
