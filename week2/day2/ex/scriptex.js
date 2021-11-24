let str = prompt('please enter a verb');

if(str.length>=3){
 if (!str.endsWith('ing')){      // ot str.sudstr(str.length-3) !='ing'
    str = str + 'ing';

}else if(str.endsWith('ing')){
    str = str + 'ly';
}
}