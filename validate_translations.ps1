<#
中文语言文件验证脚本
#>

$zh_file = "languages/built-in/zh-cn.yml"

# 检查文件是否存在
if (-not (Test-Path $zh_file)) {
    Write-Host "❌ 中文语言文件不存在: $zh_file" -ForegroundColor Red
    exit 1
}

# 读取文件内容
$content = Get-Content $zh_file -Raw
$lines = Get-Content $zh_file

Write-Host "📁 开始验证中文语言文件: $zh_file" -ForegroundColor Cyan

# 1. 检查YAML分隔符
if ($content.Trim().StartsWith('---')) {
    Write-Host "✅ 文件开头包含YAML分隔符" -ForegroundColor Green
} else {
    Write-Host "❌ 文件缺少YAML分隔符" -ForegroundColor Red
}

# 2. 检查基本翻译项
$basic_translations = @('start', 'error', 'help', 'module')
$missing_basic = @()

foreach ($key in $basic_translations) {
    $pattern = "\n$key:\s"
    if (-not ($content -match $pattern)) {
        $missing_basic += $key
    }
}

if ($missing_basic.Count -gt 0) {
    Write-Host "❌ 缺少基本翻译项: $($missing_basic -join ', ')" -ForegroundColor Red
} else {
    Write-Host "✅ 所有基本翻译项都存在" -ForegroundColor Green
}

# 3. 统计信息
$total_lines = $lines.Count
$comment_lines = ($lines | Where-Object { $_.Trim().StartsWith('#') }).Count
$translation_lines = ($lines | Where-Object { $_ -match ':' -and -not $_.Trim().StartsWith('#') -and -not $_.Trim().StartsWith('---') }).Count

Write-Host "\n📊 文件统计信息:" -ForegroundColor Cyan
Write-Host "   总行数: $total_lines" -ForegroundColor Yellow
Write-Host "   翻译项数量: $translation_lines" -ForegroundColor Yellow
Write-Host "   注释行数: $comment_lines" -ForegroundColor Yellow

# 4. 检查语法错误
$error_count = 0

for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i].Trim()
    $line_number = $i + 1
    
    if ($line -and $line -match ':' -and -not $line.StartsWith('#') -and -not $line.StartsWith('---')) {
        $parts = $line.Split(':', 2)
        $key_part = $parts[0].Trim()
        $value_part = $parts[1].Trim()
        
        # 检查键名
        if (-not $key_part -or $key_part -match '\s') {
            Write-Host "❌ 第 $line_number 行: 键名 '$key_part' 包含空格或为空" -ForegroundColor Red
            $error_count++
        }
        
        # 检查值
        if (-not $value_part -and ($parts[1].Trim() -ne '')) {
            Write-Host "❌ 第 $line_number 行: 翻译值为空" -ForegroundColor Red
            $error_count++
        }
    }
}

if ($error_count -eq 0) {
    Write-Host "✅ 未发现明显的语法错误" -ForegroundColor Green
} else {
    Write-Host "❌ 发现 $error_count 个潜在的语法错误" -ForegroundColor Red
}

# 5. 检查文件编码
$encoding = (Get-Content $zh_file -Encoding Byte -TotalCount 3)
if ($encoding[0] -eq 239 -and $encoding[1] -eq 187 -and $encoding[2] -eq 191) {
    Write-Host "❌ 文件使用了UTF-8 BOM编码，建议使用无BOM的UTF-8编码" -ForegroundColor Yellow
} else {
    Write-Host "✅ 文件编码检查通过" -ForegroundColor Green
}

Write-Host "\n🎉 验证完成！" -ForegroundColor Green