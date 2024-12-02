
$outfileName = "dev-report-1.csv"
$files = Get-ChildItem -Filter *.md "C:\{PATH OF THE FOLDER WHERE FILES ARE AVAILABLE}"
Set-Location -Path "{PATH OF REPO WHERE CLONED}"
echo "FileName,Days-Ago,Modified-Date,User,Url,Tags" >> $outfileName

foreach ($f in $files) {
    try {
        $tags = GetTags $f.FullName;
        $datefile = git log -1 --pretty="format:%cs,%al" .\tools\$f
        #$daysAgo = ((Get-Date).Date - ([datetime]$datefile.split(",")[0]).Date).Days
        Write-Host "$f,$daysAgo $datefile, $f,$tags"
        $daysago = (git log -1 --pretty="format:%ar" .\tools\$f).Replace(',','')
        echo "$f,$daysAgo,$datefile,$f,$tags" >> $outfileName
    }
    catch {
        Write-Host "Error occured" -BackgroundColor Darkred
    }
}

Function GetTags($filename) {
    try {
        $tag = Get-Content $filename | Select-String -Pattern "tags: " -CaseSensitive
        return $tag.ToString().Replace('tags: ', '').Replace(',', ';')
    }
    catch {
        Write-Host "Error occured" -BackgroundColor Darkred
    }
}
