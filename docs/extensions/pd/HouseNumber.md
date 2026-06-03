---
search:
  boost: 10.0
---

# Class: HouseNumber 


_Information about house or apartment number as a location_



<div data-search-exclude markdown="1">



URI: [pd:HouseNumber](https://w3id.org/lmodel/dpv/pd/HouseNumber)





```mermaid
 classDiagram
    class HouseNumber
    click HouseNumber href "../HouseNumber/"
      DpvLocation <|-- HouseNumber
        click DpvLocation href "../DpvLocation/"
      PhysicalAddress <|-- HouseNumber
        click PhysicalAddress href "../PhysicalAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
            * **HouseNumber** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:HouseNumber](https://w3id.org/lmodel/dpv/pd/HouseNumber) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* House Number




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#HouseNumber |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:HouseNumber |
| native | pd:HouseNumber |
| exact | dpv_pd:HouseNumber, dpv_pd_owl:HouseNumber |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HouseNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HouseNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about house or apartment number as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- House Number
exact_mappings:
- dpv_pd:HouseNumber
- dpv_pd_owl:HouseNumber
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:HouseNumber

```
</details>

### Induced

<details>
```yaml
name: HouseNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HouseNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about house or apartment number as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- House Number
exact_mappings:
- dpv_pd:HouseNumber
- dpv_pd_owl:HouseNumber
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:HouseNumber

```
</details></div>