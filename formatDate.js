var reformatDate = function(date) {
    
    let newDate = date.split(' ')
    let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    let ans = ''
    let day = newDate[0].replace(/[^0-9]+/, '')
    
    let index = months.indexOf(newDate[1])+1
      
    if (day.length == 1) {
       day = '0' + day
    }
    
    if (index.toString().length == 1) {
       index = '0' + index
    }
    
    ans += newDate[2] + '-'
    ans += index + '-'
    ans += day
    
    return ans
};
