// 便利関数(jqueryに依存しないため)
// function _(id) { return document.getElementById(id); }
// 成功
function success(pos){
    let lat = pos.coords.latitude;
    let lng = pos.coords.longitude;

    let lat6 = lat * 1000;
    let lng6 = lng * 1000;

    lat6 = Math.floor(lat6) / 1000;
    lng6 = Math.floor(lng6) / 1000;

    document.getElementById("lat6lng6").innerHTML = lat6 + lng6;
    document.getElementById("getlat6").innerHTML = lat6;
    document.getElementById("getlng6").innerHTML = lng6;

    // alert("緯度："+lat6+" 経度："+lng6+ "精度6");
  }
// 失敗
function fail(){
	// エラーコードのメッセージを定義
    const errorMessage = {
        0: "原因不明のエラーが発生しました…。",
        1: "位置情報の取得が許可されませんでした…。",
        2: "電波状況などで位置情報が取得できませんでした…。",
        3: "位置情報の取得に時間がかかり過ぎてタイムアウトしました…。",
    };

    // エラーコードに合わせたエラー内容をアラート表示
	alert( errorMessage[error.code] ) ;
}
// 取得
function result() {
    navigator.geolocation.getCurrentPosition(success,fail);
}
