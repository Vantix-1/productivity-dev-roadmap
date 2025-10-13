import os

print("🧹 Task Cleaner Utility")
folder = input("Enter folder path to clean: ")

# File types to remove
junk_extensions = [".tmp", ".log", ".txt", ".bak"]

deleted_files = 0

if os.path.exists(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path) and any(filename.endswith(ext) for ext in junk_extensions):
            os.remove(file_path)
            deleted_files += 1
            print(f"Removed: {filename}")
else:
    print("❌ Folder not found, please check path.")

print(f"\n✅ Cleanup complete. {deleted_files} junk files removed.")
