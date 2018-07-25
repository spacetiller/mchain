#include <cstdio.h>
#include <iostream.h>
#include <cmath.h>
#include <cstdlib.h>


using namespace std;
struct shu
{
	int num0;
	int num1;
};




int hashzhi(int x, int a, int mod) //底数为a，模数为mod
{
	int k = 1;
	for (int i = 0; i < x; i++) {
		k = (k*a) % mod;
	}
	return k;
}


int binaryweishu(int x) //数转化成二进制数的位数
{
	int k = 1;
	
	
	while (x > 1) {
		x = x / 2;
		k++;
	}
	return k;
}


void binary(int x, int a[]) //将数转化成二进制存进数组a[]中，其中a[0]存的是最低位
{
int i = 0;
while (x > 0) {


if (x % 2 == 0) {
a[i] = 0;
}
else {
a[i] = 1;
}
i++;
x = x / 2;
}
}


int main()
{
	int a, mod;
	cout << "请输入单向函数的底数a和模值mod：" << endl;
	cin >> a >> mod;
	cout << "请输入明文消息m：" << endl;
	int m;
	cin >> m;
	int n;
	cout << "请输入明文消息的长度n：" << endl;
	cin >> n;
	int mw[10];
	for (int i = 0; i < 10; i++) {
		mw[i] = 0;
	}
	binary(m, mw);
	/*for(int i=0;i<n;i++0{
	cout<<mw[i];<<endl;
	}
	*/
	shu y[10], z[10];
	//y为私钥数组，z为公钥数组
	cout << "请输入私钥：" << endl;
	for (int i = 0; i < n; i++) {
		cin >> y[i].num0 >> y[i].num1;
	}
	int k1, k2;
	for (int i = 0; i < n; i++) {
	
		k1 = hashzhi(y[i].num0, a, mod);
		z[i].num0 = k1;
		k2 = hashzhi(y[i].num1, a, mod);
		z[i].num1 = k2;
	}
	//生成签名：
	cout << "生成的签名为：" << endl;
	for (int i = 0; i < n; i++) {
		if (mw[i] == 0) {
			cout << y[i].num0 << endl;
		}
		else {
			cout << y[i].num1 << endl;
		}
	}
	//签名验证：
	int sign[10];  //接收方需验证的签名存在此处
	for (int i = 0; i < n; i++) {
		if (mw[i] == 0) {
			sign[i] = z[i].num0;
		}else {
			sign[i]= z[i].num1;
		}
	}
	cout << "**********************************************" << endl;
	cout << "请输入需验证的消息：" << endl;
	int m1;
	cin >> m1;
	int mw1[10];
	for (int i = 0; i < 10; i++) {
		mw1[i] = 0;
	}
	binary(m1, mw1);
	int flag = 0;
	for (int i = 0; i < n; i++) {
		if (mw1[i] == 0) {
			if (z[i].num0 != sign[i]) {
				flag = 1;
				cout << "验证不通过！" << endl;
			}
		}else {
			if (z[i].num1 != sign[i]) {
				flag = 1;
				cout << "验证不通过！" << endl;
			}
		}
	}
	if (flag == 0) {
		cout << "验证通过！" << endl;
	}
	return 0;
}
