from functions.get_file_content import get_file_content

print(f"lorem.txt length: {len(get_file_content("calculator", "lorem.txt"))}")
print(f"lorem.txt truncated: {'truncated' in (get_file_content("calculator", "lorem.txt"))}")

main = get_file_content("calculator", "main.py")
print(main)

pkg_calculator = get_file_content("calculator", "pkg/calculator.py")
print(pkg_calculator)

bin_cat = get_file_content("calculator", "/bin/cat")
print(bin_cat)

pkg_dne = get_file_content("calculator", "pkg/does_not_exist.py")
print(pkg_dne)
