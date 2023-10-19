# related_objects_data 為 network_data.json的內容
related_objects_data = {
    "network_traffic": {
        "network-traffic--3951958d-ca23-5192-be88-5a4e373d57d8": {
            "src_ref": "ipv4-addr--53fbc2f7-c1f2-5842-a1ad-c6c3c613995d",
            "dst_ref": "ipv4-addr--bff6db45-23a0-5fa6-9b09-72e6ee35988e",
            "src_port": 443,
            "dst_port": 21
        },
        "network-traffic--f7dd8d38-e5b3-5bc1-a416-dcf8040d6973": {
            "src_ref": "ipv4-addr--6ca7a96d-f107-57d1-a8ca-169f530db8a5",
            "dst_ref": "ipv6-addr--85a85a8c-ee99-5722-946d-3c3a3270fc6f",
            "src_port": 160,
            "dst_port": 443
        },
        "network-traffic--2f0bb1c5-4b1f-5d0d-9980-d4f0fd20c6e6": {
            "src_ref": "domain-name--83a85d64-4fd7-5b81-ba56-b4f703c45a07",
            "dst_ref": "domain-name--0d5ef4f4-83c5-5e42-8380-5323f8407b2a",
            "src_port": "",
            "dst_port": ""
        }
    },
    "ipv4_addr": {
        "ipv4-addr--53fbc2f7-c1f2-5842-a1ad-c6c3c613995d": "222.33.1.23",
        "ipv4-addr--bff6db45-23a0-5fa6-9b09-72e6ee35988e": "10.10.10.3",
        "ipv4-addr--6ca7a96d-f107-57d1-a8ca-169f530db8a5": "192.24.44.44"
    },
    "ipv6_addr": {
        "ipv6-addr--85a85a8c-ee99-5722-946d-3c3a3270fc6f": "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    },
    "domain_name": {
        "domain-name--83a85d64-4fd7-5b81-ba56-b4f703c45a07": "cluster789",
        "domain-name--0d5ef4f4-83c5-5e42-8380-5323f8407b2a": "abc.com"
    }
}
_network_data = {
    "src": list(),
    "Source IPv6 Address": list(),
    "shost": list(),
    "spt": list(),
    "dst": list(),
    "Destination IPv6 Address": list(),
    "dhost": list(),
    "dpt": list()
}
_ip_list = list()
_ip_data = {
    "src": "",
    "Source IPv6 Address": "",
    "shost": "",
    "spt": "",
    "dst": "",
    "Destination IPv6 Address": "",
    "dhost": "",
    "dpt": ""
}

ref_type_mapping = {
    "ipv4-addr": ("ipv4_addr", "src", "dst"),
    "ipv6-addr": ("ipv6_addr", "Source IPv6 Address", "Destination IPv6 Address"),
    "domain-name": ("domain_name", "shost", "dhost")
}

for network_traffic_id, network_traffic_obj in related_objects_data["network_traffic"].items():
    src_ip_ref = network_traffic_obj["src_ref"]
    src_ref_type = network_traffic_obj["src_ref"].split("--")[0]
    dst_ip_ref = network_traffic_obj["dst_ref"]
    dst_ref_type = network_traffic_obj["dst_ref"].split("--")[0]
    ip_dict = _ip_data.copy()

    if src_ref_type in ref_type_mapping:
        network_type, src_key, dst_key = ref_type_mapping[src_ref_type]
        src_ip = related_objects_data[network_type].get(src_ip_ref, "")

        ip_dict[src_key] = src_ip

    if dst_ref_type in ref_type_mapping:
        network_type, src_key, dst_key = ref_type_mapping[dst_ref_type]
        dst_ip = related_objects_data[network_type].get(dst_ip_ref, "")
        ip_dict[dst_key] = dst_ip

    ip_dict["spt"] = str(network_traffic_obj.get("src_port", ""))
    ip_dict["dpt"] = str(network_traffic_obj.get("dst_port", ""))

    for k,v in ip_dict.items():
        _network_data[k].append(v)

    _ip_list.append(ip_dict)

_network_data = {key: val_list for key, val_list in _network_data.items() if any(val_list)}

print(_network_data)  # result1.json
print(_ip_list)       # result2.json