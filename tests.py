from functions.get_files_info import get_files_info

print("Testing get_files_info function:")
print()

# Test 1: List contents of calculator directory (current directory)
print("Result for current directory:")
result = get_files_info("calculator", ".")
print(result)
print()

# Test 2: List contents of calculator/pkg directory
print("Result for 'pkg' directory:")
result = get_files_info("calculator", "pkg")
print(result)
print()

# Test 3: Try to access /bin directory (should return error)
print("Result for '/bin' directory:")
result = get_files_info("calculator", "/bin")
print(result)
print()

# Test 4: Try to access parent directory (should return error)
print("Result for '../' directory:")
result = get_files_info("calculator", "../")
print(result)
print()