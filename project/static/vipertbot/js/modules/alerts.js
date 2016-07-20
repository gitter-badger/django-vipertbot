export function AlertSuccess(content, title = "Success", timeout = 4000, color = "#739E73", icon = "fa fa-thumbs-up bounce animated") {
    $.smallBox({
        title: title,
        content: content,
        color: color,
        iconSmall: icon,
        timeout: 4000
    });
}

export function AlertError(content, title="Error", num = 1, timeout = 6000, color = "#C46A69", icon = "fa fa-warning shake animated") {
    $.bigBox({
        title: title,
        content: content,
        color: color,
        icon: icon,
        number: num,
        timeout: timeout
    });
}