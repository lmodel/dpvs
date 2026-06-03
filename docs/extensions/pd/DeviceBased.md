---
search:
  boost: 10.0
---

# Class: DeviceBased 


_Information about devices_



<div data-search-exclude markdown="1">



URI: [pd:DeviceBased](https://w3id.org/lmodel/dpv/pd/DeviceBased)





```mermaid
 classDiagram
    class DeviceBased
    click DeviceBased href "../DeviceBased/"
      Tracking <|-- DeviceBased
        click Tracking href "../Tracking/"
      

      DeviceBased <|-- BrowserFingerprint
        click BrowserFingerprint href "../BrowserFingerprint/"
      DeviceBased <|-- DeviceSoftware
        click DeviceSoftware href "../DeviceSoftware/"
      DeviceBased <|-- IPAddress
        click IPAddress href "../IPAddress/"
      DeviceBased <|-- MACAddress
        click MACAddress href "../MACAddress/"
      

      
```





## Inheritance
* [Tracking](Tracking.md)
    * **DeviceBased**
        * [BrowserFingerprint](BrowserFingerprint.md)
        * [DeviceSoftware](DeviceSoftware.md)
        * [IPAddress](IPAddress.md)
        * [MACAddress](MACAddress.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DeviceBased](https://w3id.org/lmodel/dpv/pd/DeviceBased) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Device Based




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DeviceBased |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DeviceBased |
| native | pd:DeviceBased |
| exact | dpv_pd:DeviceBased, dpv_pd_owl:DeviceBased |
| related | svd:Computer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeviceBased
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceBased
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about devices
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Based
exact_mappings:
- dpv_pd:DeviceBased
- dpv_pd_owl:DeviceBased
related_mappings:
- svd:Computer
is_a: Tracking
class_uri: pd:DeviceBased

```
</details>

### Induced

<details>
```yaml
name: DeviceBased
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DeviceBased
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about devices
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Device Based
exact_mappings:
- dpv_pd:DeviceBased
- dpv_pd_owl:DeviceBased
related_mappings:
- svd:Computer
is_a: Tracking
class_uri: pd:DeviceBased

```
</details></div>