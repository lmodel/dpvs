---
search:
  boost: 10.0
---

# Class: City 


_Information about city as a location_



<div data-search-exclude markdown="1">



URI: [pd:City](https://w3id.org/lmodel/dpv/pd/City)





```mermaid
 classDiagram
    class City
    click City href "../City/"
      DpvLocation <|-- City
        click DpvLocation href "../DpvLocation/"
      PhysicalAddress <|-- City
        click PhysicalAddress href "../PhysicalAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
            * **City** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:City](https://w3id.org/lmodel/dpv/pd/City) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* City




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#City |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:City |
| native | pd:City |
| exact | dpv_pd:City, dpv_pd_owl:City |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: City
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#City
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about city as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- City
exact_mappings:
- dpv_pd:City
- dpv_pd_owl:City
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:City

```
</details>

### Induced

<details>
```yaml
name: City
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#City
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about city as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- City
exact_mappings:
- dpv_pd:City
- dpv_pd_owl:City
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:City

```
</details></div>