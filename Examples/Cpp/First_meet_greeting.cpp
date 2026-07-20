#include <iostream>
#include <string>
#include <windows.h>

int main() {
    // 讓 Windows Console 使用 UTF-8，中文可正常顯示。
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);

    std::string name;

    std::cout << "請輸入你的名字: ";
    std::getline(std::cin, name);

    if (name.empty()) {
        std::cout << "你沒有輸入名字。\n";
        return 1;
    }

    std::cout << name << " 你好! 很高興認識你.\n";

    return 0;
}