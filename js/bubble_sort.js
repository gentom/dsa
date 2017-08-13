var list = [];

var listsize = 50
for (i = 1; i <= listsize; i++) {
    if (i < 4) {
        var rand = Math.floor(Math.random() * 2);
        if (rand == 1) {
            list.push(i);
        } else if (rand == 0) {
            list.unshift(i);
        }
    } else {
        len = list.length + 1;
        var rand = Math.floor(Math.random() * (len - 0) + 0);
        list.splice(rand, 0, i)
    }
}

print(list);

for (var i = 0; i < list.length; i++) {
    for (var j = list.length - 1; j > i; j--) {
        if (list[j] < list[j - 1]) {
            var tmp = list[j];
            list[j] = list[j - 1];
            list[j - 1] = tmp;
        }
    }
}

print(list);