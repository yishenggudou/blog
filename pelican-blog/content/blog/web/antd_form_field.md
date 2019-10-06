Title: antd自定义表单元素
Date: 2019-10-06 22:00
Category: web
Tags: antd, web, react
Summary: antd自定义表单元素,扩展表单列
Status: published

# 引言

# 方案

## 定义props

```

export interface ICodeEditorFieldProps {
  value: string;
  language: string;
  onChange: (value: string) => void
}

```

> value 和 onChange 必须


## 设计内部state

```
  state: any = {
    value: this.props.value ? this.props.value : (this.props.defaultValue || ''),
  };
```

## 完整例子

```
import React, { Component } from 'react';
import MonacoEditor from 'react-monaco-editor';


export interface ICodeEditorFieldProps {
  value: string;
  defaultValue: string;
  language: string;
  width?: number;
  height?: number;
  options?: object;
  onChange: (value: string) => void
}


class CodeEditorField extends Component<ICodeEditorFieldProps, any> {
  state: any = {
    value: this.props.value ? this.props.value : (this.props.defaultValue || ''),
  };

  public get componentDidMount(): void {
    const { value } = this.props;
    if (value) {
      this.setState({ value });
    }
  }

  private onChange(value: string, e: any): void {
    if (this.props.onChange) {
      this.setState({ value }, () => {
        this.props.onChange(value);
      });
    }
  }

  render() {
    const { value } = this.state;
    const { language, options, width, height } = this.props;
    return <MonacoEditor
      width={width || '100%'}
      height={height || '200'}
      language={language}
      theme="vs-dark"
      value={value}
      options={options || {}}
      onChange={this.onChange.bind(this)}
    />;
  }
}

export default CodeEditorField;
```

## 和form结合用



# 参考

1. [antd-Input](https://github.com/ant-design/ant-design/blob/master/components/input/Input.tsx)

