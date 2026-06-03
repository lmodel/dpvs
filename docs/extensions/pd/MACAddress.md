---
search:
  boost: 10.0
---

# Class: MACAddress 


_Information about the Media Access Control (MAC) address of a device_



<div data-search-exclude markdown="1">



URI: [pd:MACAddress](https://w3id.org/lmodel/dpv/pd/MACAddress)





```mermaid
 classDiagram
    class MACAddress
    click MACAddress href "../MACAddress/"
      DeviceBased <|-- MACAddress
        click DeviceBased href "../DeviceBased/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DeviceBased](DeviceBased.md)
        * **MACAddress**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:MACAddress](https://w3id.org/lmodel/dpv/pd/MACAddress) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* MAC Address




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#MACAddress |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:MACAddress |
| native | pd:MACAddress |
| exact | dpv_pd:MACAddress, dpv_pd_owl:MACAddress |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MACAddress
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MACAddress
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the Media Access Control (MAC) address of a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- MAC Address
exact_mappings:
- dpv_pd:MACAddress
- dpv_pd_owl:MACAddress
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DeviceBased
class_uri: pd:MACAddress

```
</details>

### Induced

<details>
```yaml
name: MACAddress
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MACAddress
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the Media Access Control (MAC) address of a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- MAC Address
exact_mappings:
- dpv_pd:MACAddress
- dpv_pd_owl:MACAddress
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DeviceBased
class_uri: pd:MACAddress

```
</details></div>