<#
扫描 pagermaid/ 目录下的所有 Python 文件，找出硬编码的中文字符串
并与 languages/built-in/zh-cn.yml 进行对比
#>

Write-Host "🔍 扫描 pagermaid/ 目录中的硬编码字符串..." -ForegroundColor Cyan

# 获取所有Python文件
$pythonFiles = Get-ChildItem -Path "pagermaid" -Recurse -Filter "*.py" -File

Write-Host "📁 找到 $($pythonFiles.Count) 个 Python 文件" -ForegroundColor Yellow

# 存储硬编码字符串
$hardcodedStrings = @{}

foreach ($file in $pythonFiles) {
    $content = Get-Content -Path $file.FullName -Raw

    # 匹配双引号中的中文字符串
    $doubleQuotes = $content | Select-String -Pattern '"[^"]{2,50}[\u4e00-\u9fa5]+[^"]{0,50}[^"]*"' -AllMatches

    if ($doubleQuotes) {
        foreach ($match in $doubleQuotes.Matches) {
            $cleanStr = $match.Value.Trim('"').Trim()
            if ($cleanStr.Length -gt 1 -and $cleanStr -notmatch '^\$\{|^lang\(|^\w+\(') {
                if (-not $hardcodedStrings.ContainsKey($cleanStr)) {
                    $hardcodedStrings[$cleanStr] = @()
                }
                $hardcodedStrings[$cleanStr] += $file.FullName
            }
        }
    }

    # 匹配单引号中的中文字符串
    $singleQuotes = $content | Select-String -Pattern "'[^']{2,50}[\u4e00-\u9fa5]+[^']{0,50}[^']*'" -AllMatches

    if ($singleQuotes) {
        foreach ($match in $singleQuotes.Matches) {
            $cleanStr = $match.Value.Trim("'").Trim()
            if ($cleanStr.Length -gt 1 -and $cleanStr -notmatch '^\$\{|^lang\(|^\w+\(') {
                if (-not $hardcodedStrings.ContainsKey($cleanStr)) {
                    $hardcodedStrings[$cleanStr] = @()
                }
                $hardcodedStrings[$cleanStr] += $file.FullName
            }
        }
    }
}

Write-Host "`n📊 发现 $($hardcodedStrings.Count) 个潜在的硬编码字符串" -ForegroundColor Yellow
Write-Host "=" * 80 -ForegroundColor Gray

# 加载中文语言文件
Write-Host "`n🔍 加载中文语言文件..." -ForegroundColor Cyan

try {
    $zhContent = Get-Content -Path "languages/built-in/zh-cn.yml" -Raw
    $zhLines = Get-Content -Path "languages/built-in/zh-cn.yml"

    # 提取所有翻译值
    $zhValues = @()
    foreach ($line in $zhLines) {
        if ($line -match ':\s*"[^"]*"' -or $line -match ":\s*'[^']*'") {
            $parts = $line.Split(':', 2)
            if ($parts.Count -eq 2) {
                $value = $parts[1].Trim().Trim('"').Trim("'")
                if ($value) {
                    $zhValues += $value
                }
            }
        }
    }

    Write-Host "📊 中文语言文件中包含 $($zhValues.Count) 个翻译项" -ForegroundColor Yellow

    # 对比硬编码字符串和语言文件
    $foundInLang = @()
    $missingInLang = @{}

    foreach ($item in $hardcodedStrings.GetEnumerator()) {
        $found = $false
        foreach ($zhValue in $zhValues) {
            if ($zhValue -eq $item.Key) {
                $found = $true
                break
            }
        }
        if ($found) {
            $foundInLang += $item.Key
        } else {
            $missingInLang[$item.Key] = $item.Value
        }
    }

    Write-Host "`n✅ 已在语言文件中找到: $($foundInLang.Count) 个" -ForegroundColor Green
    Write-Host "❌ 未在语言文件中找到: $($missingInLang.Count) 个" -ForegroundColor Red

    if ($missingInLang.Count -gt 0) {
        Write-Host "`n" -ForegroundColor Gray
        Write-Host "⚠️  以下硬编码字符串未在中文语言文件中找到对应的翻译:" -ForegroundColor Yellow
        Write-Host "=" * 80 -ForegroundColor Gray

        $counter = 0
        foreach ($item in $missingInLang.GetEnumerator()) {
            $counter++
            Write-Host "`n$counter. `"$($item.Key)`"" -ForegroundColor White
            Write-Host "   文件: $($item.Value -join ', ')" -ForegroundColor Gray
        }
    }

} catch {
    Write-Host "❌ 加载语言文件失败: $_" -ForegroundColor Red
}

Write-Host "`n🎉 扫描完成！" -ForegroundColor Green