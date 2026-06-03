---
search:
  boost: 10.0
---

# Class: DeviceSoftware 


_Information about software on or related to a device_



<div data-search-exclude markdown="1">



URI: [pd:DeviceSoftware](https://w3id.org/lmodel/dpv/pd/DeviceSoftware)





```mermaid
 classDiagram
    class DeviceSoftware
    click DeviceSoftware href "../DeviceSoftware/"
      DeviceBased <|-- DeviceSoftware
        click DeviceBased href "../DeviceBased/"
      

      DeviceSoftware <|-- DeviceApplications
        click DeviceApplications href "../DeviceApplications/"
      DeviceSoftware <|-- DeviceOperatingSystem
        click DeviceOperatingSystem href "../DeviceOperatingSystem/"
      

      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DeviceBased](DeviceBased.md)
        * **DeviceSoftware**
            * [DeviceApplications](DeviceApplications.md)
            * [DeviceOperatingSystem](DeviceOperatingSystem.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DeviceSoftware](https://w3id.org/lmodel/dpv/pd/DeviceSoftware) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Device Software




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DeviceSoftware |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DeviceSoftware |
| native | pd:DeviceSoftware |
| exact | dpv_pd:DeviceSoftware, dpv_pd_owl:DeviceSoftware |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeviceSoftware
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceSoftware
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about software on or related to a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Software
exact_mappings:
- dpv_pd:DeviceSoftware
- dpv_pd_owl:DeviceSoftware
is_a: DeviceBased
class_uri: pd:DeviceSoftware

```
</details>

### Induced

<details>
```yaml
name: DeviceSoftware
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceSoftware
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about software on or related to a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Software
exact_mappings:
- dpv_pd:DeviceSoftware
- dpv_pd_owl:DeviceSoftware
is_a: DeviceBased
class_uri: pd:DeviceSoftware

```
</details></div>