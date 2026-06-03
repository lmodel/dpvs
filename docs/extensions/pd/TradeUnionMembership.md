---
search:
  boost: 10.0
---

# Class: TradeUnionMembership 


_Information about trade union memberships and related topics_



<div data-search-exclude markdown="1">



URI: [pd:TradeUnionMembership](https://w3id.org/lmodel/dpv/pd/TradeUnionMembership)





```mermaid
 classDiagram
    class TradeUnionMembership
    click TradeUnionMembership href "../TradeUnionMembership/"
      GroupMembership <|-- TradeUnionMembership
        click GroupMembership href "../GroupMembership/"
      
      
```





## Inheritance
* **TradeUnionMembership** [ [GroupMembership](GroupMembership.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:TradeUnionMembership](https://w3id.org/lmodel/dpv/pd/TradeUnionMembership) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Trade Union Membership




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#TradeUnionMembership |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:TradeUnionMembership |
| native | pd:TradeUnionMembership |
| exact | dpv_pd:TradeUnionMembership, dpv_pd_owl:TradeUnionMembership |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TradeUnionMembership
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TradeUnionMembership
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about trade union memberships and related topics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Trade Union Membership
exact_mappings:
- dpv_pd:TradeUnionMembership
- dpv_pd_owl:TradeUnionMembership
mixins:
- GroupMembership
class_uri: pd:TradeUnionMembership

```
</details>

### Induced

<details>
```yaml
name: TradeUnionMembership
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TradeUnionMembership
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about trade union memberships and related topics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Trade Union Membership
exact_mappings:
- dpv_pd:TradeUnionMembership
- dpv_pd_owl:TradeUnionMembership
mixins:
- GroupMembership
class_uri: pd:TradeUnionMembership

```
</details></div>