---
search:
  boost: 10.0
---

# Class: Street 


_Information about street as a location_



<div data-search-exclude markdown="1">



URI: [pd:Street](https://w3id.org/lmodel/dpv/pd/Street)





```mermaid
 classDiagram
    class Street
    click Street href "../Street/"
      DpvLocation <|-- Street
        click DpvLocation href "../DpvLocation/"
      PhysicalAddress <|-- Street
        click PhysicalAddress href "../PhysicalAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
            * **Street** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Street](https://w3id.org/lmodel/dpv/pd/Street) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Street




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Street |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Street |
| native | pd:Street |
| exact | dpv_pd:Street, dpv_pd_owl:Street |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Street
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Street
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about street as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Street
exact_mappings:
- dpv_pd:Street
- dpv_pd_owl:Street
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:Street

```
</details>

### Induced

<details>
```yaml
name: Street
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Street
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about street as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Street
exact_mappings:
- dpv_pd:Street
- dpv_pd_owl:Street
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:Street

```
</details></div>