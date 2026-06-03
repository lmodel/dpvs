---
search:
  boost: 10.0
---

# Class: IPAddress 


_Information about the Internet Protocol (IP) address of a device_



<div data-search-exclude markdown="1">



URI: [pd:IPAddress](https://w3id.org/lmodel/dpv/pd/IPAddress)





```mermaid
 classDiagram
    class IPAddress
    click IPAddress href "../IPAddress/"
      DeviceBased <|-- IPAddress
        click DeviceBased href "../DeviceBased/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DeviceBased](DeviceBased.md)
        * **IPAddress**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:IPAddress](https://w3id.org/lmodel/dpv/pd/IPAddress) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* IP Address




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#IPAddress |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:IPAddress |
| native | pd:IPAddress |
| exact | dpv_pd:IPAddress, dpv_pd_owl:IPAddress |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IPAddress
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IPAddress
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the Internet Protocol (IP) address of a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- IP Address
exact_mappings:
- dpv_pd:IPAddress
- dpv_pd_owl:IPAddress
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DeviceBased
class_uri: pd:IPAddress

```
</details>

### Induced

<details>
```yaml
name: IPAddress
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IPAddress
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the Internet Protocol (IP) address of a device
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- IP Address
exact_mappings:
- dpv_pd:IPAddress
- dpv_pd_owl:IPAddress
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DeviceBased
class_uri: pd:IPAddress

```
</details></div>