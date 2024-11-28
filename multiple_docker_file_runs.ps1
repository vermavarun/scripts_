$start = get-date "2024-10-24"
$end = Get-Date "2024-10-27"
$portal = ""

while($start -ne $end){

    $containerName = $portal + "_" + $start.ToString("yyyy-MM-dd")
    docker `
    run -d --rm --name $containerName `
    -v /Users/xxxxx/Desktop/xxx/logs:/application/logs `
    -e SOME_ENV_VAL_1="" `
    -e SOME_ENV_VAL_2="" `
    daystar `
    --SOME_PARAMETER_FOR_DOCKER_FILE "" `
    --SOME__OTHER_PARAMETER_FOR_DOCKER_FILE $portal `
    $start = $start.AddDays(1)
    
}
