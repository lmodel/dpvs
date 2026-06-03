---
search:
  boost: 10.0
---

# Class: DeviceOperatingSystem 


_Information about the operating system (OS) or system software that_

_manages hardware or software resources._



<div data-search-exclude markdown="1">



URI: [pd:DeviceOperatingSystem](https://w3id.org/lmodel/dpv/pd/DeviceOperatingSystem)





```mermaid
 classDiagram
    class DeviceOperatingSystem
    click DeviceOperatingSystem href "../DeviceOperatingSystem/"
      DeviceSoftware <|-- DeviceOperatingSystem
        click DeviceSoftware href "../DeviceSoftware/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DeviceBased](DeviceBased.md)
        * [DeviceSoftware](DeviceSoftware.md)
            * **DeviceOperatingSystem**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DeviceOperatingSystem](https://w3id.org/lmodel/dpv/pd/DeviceOperatingSystem) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Device Operating System




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DeviceOperatingSystem |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DeviceOperatingSystem |
| native | pd:DeviceOperatingSystem |
| exact | dpv_pd:DeviceOperatingSystem, dpv_pd_owl:DeviceOperatingSystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeviceOperatingSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceOperatingSystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about the operating system (OS) or system software that

  manages hardware or software resources.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Operating System
exact_mappings:
- dpv_pd:DeviceOperatingSystem
- dpv_pd_owl:DeviceOperatingSystem
is_a: DeviceSoftware
class_uri: pd:DeviceOperatingSystem

```
</details>

### Induced

<details>
```yaml
name: DeviceOperatingSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceOperatingSystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about the operating system (OS) or system software that

  manages hardware or software resources.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Operating System
exact_mappings:
- dpv_pd:DeviceOperatingSystem
- dpv_pd_owl:DeviceOperatingSystem
is_a: DeviceSoftware
class_uri: pd:DeviceOperatingSystem

```
</details></div>