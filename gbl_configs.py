s3_creds = {
    'bucket_url'        : {'incremental' : 's3a://asdasdsdas/asdasdasd/asdassd',
                           'historical'  : 's3n://sdfdsfsdf/sdfsdfdsf/sdfsdfsdf/sadsfsdafsad'},
    's3_access_key'     : "ADGAFGVTRHBTRSWV546FDGBV",
    's3_secret_key'     : "VDSnkvsMCVKSDGJRW4398jcKFnMEWRT894/t",
    's3_proxy_host'     : "proxy.abc.com",
    's3_proxy_port'     : "80",
    'num_mappers'       : "200"
}

#commit 2
s3a://asdasdsdas/asdasdasd/asdassd

#commit 3
s3a://asdasdsdas/asdasdasd/asdassd
s3n://sdfdsfsdf/sdfsdfdsf/sdfsdfsdf/sadsfsdafsad

#commit 4
s3a://asdasdsdas/asdasdasd/asdassd
s3n://sdfdsfsdf/sdfsdfdsf/sdfsdfsdf/sadsfsdafsad
ADGAFGVTRHBTRSWV546FDGBV

#commit 5
s3a://asdasdsdas/asdasdasd/asdassd
s3n://sdfdsfsdf/sdfsdfdsf/sdfsdfsdf/sadsfsdafsad
ADGAFGVTRHBTRSWV546FDGBV
"VDSnkvsMCVKSDGJRW4398jcKFnMEWRT894/t"

#commit 6
s3a://asdasdsdas/asdasdasd/asdassd
s3n://sdfdsfsdf/sdfsdfdsf/sdfsdfsdf/sadsfsdafsad
ADGAFGVTRHBTRSWV546FDGBV
"VDSnkvsMCVKSDGJRW4398jcKFnMEWRT894/t"
"proxy.abc.com"
