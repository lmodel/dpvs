---
search:
  boost: 10.0
---

# Class: AM 


_Concept representing Country of Armenia_



<div data-search-exclude markdown="1">



URI: [loc:AM](https://w3id.org/lmodel/dpv/loc/AM)





```mermaid
 classDiagram
    class AM
    click AM href "../AM/"
      AM <|-- AMAG
        click AMAG href "../AMAG/"
      AM <|-- AMAR
        click AMAR href "../AMAR/"
      AM <|-- AMAV
        click AMAV href "../AMAV/"
      AM <|-- AMER
        click AMER href "../AMER/"
      AM <|-- AMGR
        click AMGR href "../AMGR/"
      AM <|-- AMKT
        click AMKT href "../AMKT/"
      AM <|-- AMLO
        click AMLO href "../AMLO/"
      AM <|-- AMSH
        click AMSH href "../AMSH/"
      AM <|-- AMSU
        click AMSU href "../AMSU/"
      AM <|-- AMTV
        click AMTV href "../AMTV/"
      AM <|-- AMVD
        click AMVD href "../AMVD/"
      
      
```





## Inheritance
* **AM**
    * [AMAG](AMAG.md)
    * [AMAR](AMAR.md)
    * [AMAV](AMAV.md)
    * [AMER](AMER.md)
    * [AMGR](AMGR.md)
    * [AMKT](AMKT.md)
    * [AMLO](AMLO.md)
    * [AMSH](AMSH.md)
    * [AMSU](AMSU.md)
    * [AMTV](AMTV.md)
    * [AMVD](AMVD.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AM](https://w3id.org/lmodel/dpv/loc/AM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Armenia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AM |
| native | loc:AM |
| exact | dpv_loc:AM, dpv_loc_owl:AM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Armenia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Armenia
exact_mappings:
- dpv_loc:AM
- dpv_loc_owl:AM
class_uri: loc:AM

```
</details>

### Induced

<details>
```yaml
name: AM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Armenia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Armenia
exact_mappings:
- dpv_loc:AM
- dpv_loc_owl:AM
class_uri: loc:AM

```
</details></div>