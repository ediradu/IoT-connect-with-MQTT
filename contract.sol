pragma solidity ^0.8.0;

contract SensorData {
    struct Data {
        uint256 timestamp;
        string sensorType;
        string dataValue;
    }
    Data[] public dataLog;

    function addData(string memory sensorType, string memory dataValue) public {
        dataLog.push(Data(block.timestamp, sensorType, dataValue));
    }

    function getData(uint index) public view returns (uint256, string memory, string memory) {
        Data memory data = dataLog[index];
        return (data.timestamp, data.sensorType, data.dataValue);
    }
}
