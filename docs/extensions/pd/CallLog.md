---
search:
  boost: 10.0
---

# Class: CallLog 


_Information about the calls that an individual has made_



<div data-search-exclude markdown="1">



URI: [pd:CallLog](https://w3id.org/lmodel/dpv/pd/CallLog)





```mermaid
 classDiagram
    class CallLog
    click CallLog href "../CallLog/"
      Behavioural <|-- CallLog
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **CallLog**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CallLog](https://w3id.org/lmodel/dpv/pd/CallLog) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Call Log




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CallLog |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CallLog |
| native | pd:CallLog |
| exact | dpv_pd:CallLog, dpv_pd_owl:CallLog |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CallLog
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CallLog
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the calls that an individual has made
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Call Log
exact_mappings:
- dpv_pd:CallLog
- dpv_pd_owl:CallLog
is_a: Behavioural
class_uri: pd:CallLog

```
</details>

### Induced

<details>
```yaml
name: CallLog
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CallLog
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the calls that an individual has made
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Call Log
exact_mappings:
- dpv_pd:CallLog
- dpv_pd_owl:CallLog
is_a: Behavioural
class_uri: pd:CallLog

```
</details></div>