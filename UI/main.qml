import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 900
    height: 750
    title: "HelloApp"

    Text {
        anchors.centerIn: parent
        text: "Hello, World"
        font.pixelSize: 24
    }

}