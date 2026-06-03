---
search:
  boost: 10.0
---

# Class: DeviceApplications 


_Information about applications or application-like software on a device_



<div data-search-exclude markdown="1">



URI: [pd:DeviceApplications](https://w3id.org/lmodel/dpv/pd/DeviceApplications)





```mermaid
 classDiagram
    class DeviceApplications
    click DeviceApplications href "../DeviceApplications/"
      DeviceSoftware <|-- DeviceApplications
        click DeviceSoftware href "../DeviceSoftware/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DeviceBased](DeviceBased.md)
        * [DeviceSoftware](DeviceSoftware.md)
            * **DeviceApplications**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DeviceApplications](https://w3id.org/lmodel/dpv/pd/DeviceApplications) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Device Applications




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DeviceApplications |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DeviceApplications |
| native | pd:DeviceApplications |
| exact | dpv_pd:DeviceApplications, dpv_pd_owl:DeviceApplications |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeviceApplications
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceApplications
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about applications or application-like software on a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Applications
exact_mappings:
- dpv_pd:DeviceApplications
- dpv_pd_owl:DeviceApplications
is_a: DeviceSoftware
class_uri: pd:DeviceApplications

```
</details>

### Induced

<details>
```yaml
name: DeviceApplications
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceApplications
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about applications or application-like software on a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Applications
exact_mappings:
- dpv_pd:DeviceApplications
- dpv_pd_owl:DeviceApplications
is_a: DeviceSoftware
class_uri: pd:DeviceApplications

```
</details></div>