import numpy

N = 22255382023772668851018179427844169178508638456713544208965498667359965716247243217931028270320680101854437928939452335472153643094266035953797432826168426002458800906764442624308120284177094975740468163835305872963635678413995878812492729432260346481442092245748885202467992527408086207041964831622724073720751839241897580988210971776031098476500998975223039782371635291859483569580516707907602619018780393060215756966917504096971372578145138070121288608502379649804953835336933545368863853793291348412017384228807171466141787383764812064465152885522264261710104646819565161405416285530129398700414912821358924882993
M = 455054308184393892678058040417894434538147052966484655368629806848690951585316383741818991249942897131402174931069148907410409095241197004639436085265522674198117934494409967755516107042868190564732371162423204135770802585390754508661199283919569348449653439331457503898545517122035939648918370853985174413495

tmp=M**2-8*N
print(numpy.sqrt(tmp))