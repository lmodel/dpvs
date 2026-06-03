---
search:
  boost: 10.0
---

# Class: DpvRegion 


_Information about region as a location_



<div data-search-exclude markdown="1">



URI: [pd:Region](https://w3id.org/lmodel/dpv/pd/Region)





```mermaid
 classDiagram
    class DpvRegion
    click DpvRegion href "../DpvRegion/"
      DpvLocation <|-- DpvRegion
        click DpvLocation href "../DpvLocation/"
      PhysicalAddress <|-- DpvRegion
        click PhysicalAddress href "../PhysicalAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
            * **DpvRegion** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Region](https://w3id.org/lmodel/dpv/pd/Region) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Region |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Region |
| native | pd:DpvRegion |
| exact | dpv_pd:Region, dpv_pd_owl:Region |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvRegion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Region
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about region as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Region
exact_mappings:
- dpv_pd:Region
- dpv_pd_owl:Region
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:Region

```
</details>

### Induced

<details>
```yaml
name: DpvRegion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Region
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about region as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Region
exact_mappings:
- dpv_pd:Region
- dpv_pd_owl:Region
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:Region

```
</details></div>