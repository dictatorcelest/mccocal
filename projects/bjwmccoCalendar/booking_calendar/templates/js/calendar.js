/*==========================calendar 类=================================================*/ 
function calendar(date_id,cal_id,today_id)//参数一是显示年月的标签id,参数二是显示日历内容的标签id,参数三是在日历内容显示当日的样式id
{
/*
*日历类
*主要属性:当前日期年、月、日,动态的年、月、日
*主要方法：转子到上一月，转子到下一月，日历显示，时间显示
*/
this.date_id = date_id;
this.cal_id = cal_id;
this.today_id = today_id;
var today = new Date();
this.year = today.getFullYear();
this.month = today.getMonth();
this.date = today.getDate();
today = null;
this.tmp_year = this.year;
this.tmp_month = this.month;
this.tmp_date= this.date;

this.weekcn = new Array ('日','一','二','三','四','五','六'); 
this.weekcn_en = new Array ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
this.countDays = function (year,month) //根据参数一跟参数二的年月计算该月有多少天,返回就是该月的天数,一月份对0,二月份对应1,如此类推,是从0开始
    {
        var days_in_months = new Array(31,28,31,30,31,30,31,31,30,31,30,31);
        if (1 == month) return ((0 == year % 4) && (0 != (year % 100))) ||(0 == year % 400) ? 29 : 28;
        else return days_in_months[month];
    }

this.calendar = function()//日历的内容 
    {    
        var date = new Date(this.tmp_year,this.tmp_month,1);
        var date_month = date.getMonth();
        var date_year = date.getYear();
        var date_weekcn = date.getDay();//星期
        var month_days = this.countDays(date_year,date_month);
        var tmp = 1 - date_weekcn;
        var date_str="";
        //日历显示
        //排列星期的标题
         date_str+="<table>";
         for (var w=0; w<7; w++)
         {
              date_str = date_str+"<th>"+this.weekcn[w]+"</th>";//将weekcn[]修改weekcn_en[]日历标题显示为英文
         }
         for (var i=0; i<6; i++)
        {
              date_str+="<tr>";
              for (var k=0; k<7; k++)
            {
                   if ((this.year==this.tmp_year)&&(this.month == this.tmp_month)&&(this.date == tmp)) 
                    date_str+="<td id=\""+this.today_id+"\">";//判断是否是当前显示的日期是现时的日期,是则用now 的CSS 样式
                   else
                       date_str+="<td>";
                   if ((tmp>0)&&(tmp<=month_days)) date_str+=tmp;
                   //else date_str+='n/a';//这里是输出非日期内容的表格显示的内容
                   tmp++;
               date_str+="</td>";
              }
              date_str+="</tr>";
         }
        date_str+="</table>";
        return date_str;
    }
    
this.yearMonth = function ()//年月的内容
    {
        var str = this.tmp_year+"年"
        if (this.tmp_month <9) {str = str+"0"+(this.tmp_month+1)+"月";}
        else {str = str+(this.tmp_month+1)+"月";}
        return str;
    }

this.calendarShow = function ()//根据id 输出日历内容
    {
        var calendar_show = document.getElementById(this.cal_id);
        calendar_show.innerHTML = this.calendar();
    }
    
this.yearMonthShow = function ()//根据id 输出年月内容
    {
        var date_show = document.getElementById (this.date_id);
        date_show.innerHTML = this.yearMonth();
    }
    
this.nextMonth = function ()//下一月
    {
        if (this.tmp_month>=11) {this.tmp_month = 0;this.tmp_year +=1;}
        else {this.tmp_month += 1;}
        this.calendarShow();
        this.yearMonthShow();
        return false;
    }
    
this.prevMonth = function ()//上一月
    {
        if (this.tmp_month<=0) {this.tmp_month = 11;this.tmp_year -=1;}
        else {this.tmp_month -= 1;}
        this.calendarShow();
        this.yearMonthShow();
        return false;
    }

    
}
/*==========================calendar 类=================================================*/
/* 现时这个类供外部有效使用的方法(成员函数)包括以下,其它的方法(成员函数)对网页上的内容不会作出任何改变:
*    this.yearMonthShow()// 显示年月
*    this.calendarShow() // 显示日历内容
*    this.nextMonth() // 使日历转到下个月
*    this.prevMonth() // 使日历转到上个月
*/