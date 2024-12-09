# RAMMap自动清理程序（含Python源代码）

## 简介

本仓库提供了一个利用Python脚本调用命令行工具（CMD）实现RAMMap每隔一分钟自动释放内存的程序。通过双击运行`RAMMapRUN`即可启动该程序。该程序需要管理员权限才能正常运行，否则无法调用RAMMap工具。

## 功能特点

- **自动清理内存**：每隔一分钟自动调用RAMMap工具释放内存。
- **管理员权限要求**：程序需要以管理员权限运行，否则无法调用RAMMap。
- **可定制性**：包含Python源代码，用户可以根据需要自行修改和添加功能。

## 使用方法

1. **下载资源文件**：从本仓库下载资源文件。
2. **运行程序**：双击运行`RAMMapRUN`文件，程序将自动以管理员权限启动并开始每隔一分钟释放内存。
3. **管理员权限**：确保在运行程序时已授予管理员权限，否则程序将无法正常工作。

## 注意事项

- **管理员权限**：由于程序需要调用RAMMap工具，因此必须以管理员权限运行。
- **Python环境**：如果需要修改源代码，请确保本地已安装Python环境。

## 源代码说明

本程序的源代码使用Python编写，包含在资源文件中。用户可以根据自己的需求对源代码进行修改和扩展，例如调整清理频率、添加日志记录等功能。

## 贡献

欢迎大家提出改进建议或提交Pull Request，共同完善这个工具。

## 许可证

本项目采用MIT许可证，详情请参阅LICENSE文件。
